console.log("working");

// var ICE_config= {
//     'iceServers': [
//         {url:'stun:stun01.sipphone.com'},
//         {url:'stun:stun.ekiga.net'},
//         {url:'stun:stun.fwdnet.net'},
//         {url:'stun:stun.ideasip.com'},
//         {url:'stun:stun.iptel.org'},
//         {url:'stun:stun.rixtelecom.se'},
//         {url:'stun:stun.schlund.de'},
//         {url:'stun:stun.l.google.com:19302'},
//         {url:'stun:stun1.l.google.com:19302'},
//         {url:'stun:stun2.l.google.com:19302'},
//         {url:'stun:stun3.l.google.com:19302'},
//         {url:'stun:stun4.l.google.com:19302'},
//         {url:'stun:stunserver.org'},
//         {url:'stun:stun.softjoys.com'},
//         {url:'stun:stun.voiparound.com'},
//         {url:'stun:stun.voipbuster.com'},
//         {url:'stun:stun.voipstunt.com'},
//         {url:'stun:stun.voxgratia.org'},
//         {url:'stun:stun.xten.com'},
//     ]
//   }

var ICE_config=null

var labelUsername = document.querySelector('#label-username');
var usernameInput = document.querySelector('#username');
var btnJoin = document.querySelector('#btn-join');

var username;
var webSocket;
var peers = {};

function closetab(){
    close();
}

function webSocketOnMessage(event){
    var parsedData = JSON.parse(event.data);
    var peerUsername = parsedData['peer']; //username of the other peer
    var action = parsedData['action']; ///action of the other peer

    if(username == peerUsername){ //when a person receives his own message from the group
        return;
    }


    var receiver_channel_name = parsedData['message']['receiver_channel_name'];

    if(action == 'new-peer'){ // when a new peer is added to the group
        createOffer(peerUsername, receiver_channel_name);

        return;
    }
    if(action == 'new-offer'){
        offer = parsedData['message']['sdp'];
        createAnswerer(offer, peerUsername, receiver_channel_name);
        return;
    }
    if(action == "new-answer"){
        var answer = parsedData['message']['sdp'];
        var peer = peers[peerUsername][0];
        peer.setRemoteDescription(answer);
        return;
    }
}

btnJoin.addEventListener('click', ()=>{
    console.log('btn clicked');
    username = usernameInput.value // cannot be same
    // username = "Anonymous User";
    console.log('username:', username);
    if(username === '')
        return;
    usernameInput.value = "";
    usernameInput.disabled = true;
    usernameInput.style.visibility = "hidden";

    btnJoin.disabled = true;
    btnJoin.style.visibility = "hidden";
    document.querySelector('#call-joined').innerHTML = "Call Joined"
    document.querySelector('#waiting-for-caller').innerHTML = "Waiting For Caller...";
    document.querySelector('#wait-spin').classList.remove('hidden');

    var labelUsername = document.querySelector('#label-username');
    labelUsername.innerHTML = username;

    var loc = window.location;
    var wsStart = "wss://";
    
    if(loc.protocol== "https"){
        wsStart = "wss://";
    }

    // var endPoint = wsStart + loc.host + loc.pathname;
    room_name = document.querySelector('#room_name').value
    var endPoint = wsStart + loc.host + "/" + room_name + "/";
    console.log(endPoint);

    //creating a web socket -- opening of socket
    webSocket = new WebSocket(endPoint);

    //opening of socket
    webSocket.addEventListener("open", (e)=>{
        console.log('Connection opened');

        sendSignal('new-peer',{});
    });

    //on message received
    webSocket.addEventListener("message", webSocketOnMessage);

    //on close
    webSocket.addEventListener("onclose",(e)=>{
        console.log('Connection closed');
    });

    //on error in websocket
    webSocket.addEventListener("error", (e)=>{
        console.log('Error occured');
    });
})

var localStream = new MediaStream();

const constraints = {
    'video' : true,
    'audio': true,
}
const localVideo = document.querySelector('#local-video');

const btnToggleAudio = document.querySelector('#btn-toggle-audio');
const btnToggleVideo = document.querySelector('#btn-toggle-video');

var userMedia = navigator.mediaDevices.getUserMedia(constraints)
    .then(stream=>{
        localStream = stream;
        localVideo.srcObject = localStream;
        localVideo.muted = true;

        var audioTracks = stream.getAudioTracks();
        var videoTracks = stream.getVideoTracks();

        audioTracks[0].enabled =true;
        videoTracks[0].enabled =true;

        btnToggleAudio.addEventListener('click', ()=>{
            audioTracks[0].enabled = !audioTracks[0].enabled;
            if(audioTracks[0].enabled){
                btnToggleAudio.innerHTML = "<i class='bi bi-mic-fill'></i>";

                return;
            }
            btnToggleAudio.innerHTML= "<i class='bi bi-mic-mute-fill'></i>";
        })

        btnToggleVideo.addEventListener('click', ()=>{
            videoTracks[0].enabled = !videoTracks[0].enabled;
            if(videoTracks[0].enabled){
                btnToggleVideo.innerHTML = "<i class='bi bi-camera-video-fill'></i>";

                return;
            }
            btnToggleVideo.innerHTML= "<i class='bi bi-camera-video-off-fill'></i>";
        })

    })
    .catch(error =>{
        console.log('Error accessing Media Devices')
    })



function sendSignal(action, message){
    var jsonStr = JSON.stringify({
        'peer':username,
        'action': action,
        'message': message,
    })
    
    webSocket.send(jsonStr);
}

function createOffer(peerUsername, receiver_channel_name){

    var peer = new RTCPeerConnection(ICE_config); //two devices in the same network

    addLocalTracks(peer); // take local audio and video tracks and add to the peer(RTCPeerConnection)

    var dc = peer.createDataChannel('channel');
    dc.addEventListener('open',()=>{
        console.log('Connection open');
    })

    dc.addEventListener('message',dcOnMessage);

    var remoteVideo = createVideo(peerUsername);
    setOnTrack(peer, remoteVideo);

    peers[peerUsername] = [peer, dc];

    peer.addEventListener('iceconnectionstatechange',()=>{
        var iceConnectionState = peer.iceConnectionState;
        if(iceConnectionState === 'failed' || iceConnectionState === 'disconnected' || iceConnectionState === 'closed'){
            delete peers[peerUsername]
            if(iceConnectionState != 'closed'){
                peer.close();
            }
            removeVideo(remoteVideo);
        }
    })

    peer.addEventListener('icecandidate',(event)=>{
        if(event.candidate){
            console.log("New ICE Candidate:", JSON.stringify(peer.localDescription))
            document.querySelector('#waiting-for-caller').innerHTML = "";
            document.querySelector('#wait-spin').classList.add('hidden');
            console.log('Here');
            return;
        }
        sendSignal('new-offer',{
            'sdp':peer.localDescription,
            'receiver_channel_name': receiver_channel_name,
        })
    })
    peer.createOffer().then(o=> peer.setLocalDescription(o))
        .then(()=>{
            console.log('local desc set successfully');
        })
}

function createAnswerer(offer, peerUsername, receiver_channel_name){

    var peer = new RTCPeerConnection(ICE_config); //two devices in the same network

    addLocalTracks(peer); // take local audio and video tracks and add to the peer(RTCPeerConnection)


    var remoteVideo = createVideo(peerUsername);
    setOnTrack(peer, remoteVideo);

    peer.addEventListener('datachannel', e =>{
        peer.dc = e.channel;
        peer.dc.addEventListener('open',()=>{
            console.log('Connection open');
        });
    
        peer.dc.addEventListener('message',dcOnMessage);
        peers[peerUsername] = [peer, dc];
    })

    

    peer.addEventListener('iceconnectionstatechange',()=>{
        var iceConnectionState = peer.iceConnectionState;
        if(iceConnectionState === 'failed' || iceConnectionState === 'disconnected' || iceConnectionState === 'closed'){
            delete peers[peerUsername]
            if(iceConnectionState != 'closed'){
                peer.close();
            }
            removeVideo(remoteVideo);
        }
    })

    peer.addEventListener('icecandidate',(event)=>{
        if(event.candidate){
            console.log("New ICE Candidate:", JSON.stringify(peer.localDescription))
            document.querySelector('#waiting-for-caller').innerHTML = "";
            document.querySelector('#wait-spin').classList.add('hidden');

            return;
        }
        sendSignal('new-answer',{
            'sdp':peer.localDescription,
            'receiver_channel_name': receiver_channel_name,
        })
    })
    peer.setRemoteDescription(offer)
    .then(()=>{
        console.log('Remote Description set successfully for %s', peerUsername);

        return peer.createAnswer();
    })   
    .then(a=>{
        console.log("answer created");

        peer.setLocalDescription(a);
    })
}

function addLocalTracks(peer){
    localStream.getTracks().forEach(track =>{
        peer.addTrack(track, localStream);
    })

    return;
}

var messageList = document.querySelector('#message-list');
function dcOnMessage(event){
    var message = event.data;

    var li = document.createElement('li');
    li.appendChild(document.createTextNode(message));
    messageList.appendChild(li);
}

function createVideo(peerUsername){
    var videoContainer = document.querySelector('#video-container');
    var remoteVideo = document.createElement('video');
    remoteVideo.id = peerUsername + "-video";
    remoteVideo.autoplay = true;
    remoteVideo.playsInline = true;

    var videoWrapper = document.createElement('div');
    videoWrapper.classList.add('flex-object');
    videoWrapper.appendChild(remoteVideo);
    videoContainer.appendChild(videoWrapper);

    return remoteVideo;
}

function setOnTrack(peer, remoteVideo){
    var remoteStream = new MediaStream();

    remoteVideo.srcObject = remoteStream;
    peer.addEventListener('track', async(event)=>{
        remoteStream.addTrack(event.track, remoteStream)
    });
}

function removeVideo(video){
    var videoWrapper = video.parentNode;
    videoWrapper.parentNode.removeChild(videoWrapper);
    document.querySelector('#waiting-for-caller').innerHTML = "Caller Disconnected!.<br>Waiting For Caller...";
    document.querySelector('#wait-spin').classList.remove('hidden');
}