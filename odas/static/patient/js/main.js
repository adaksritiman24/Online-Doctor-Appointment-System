console.log("Main.js working");

function dateForAppointment(id){
    date = document.querySelector('#app-date-for-'+id).value;

    document.getElementById("paypal-button-container-"+id).innerHTML = "";
    document.getElementById('pay-to-proceed-'+id).style.visibility="hidden";
    document.getElementById("date-and-time-for-"+id).innerHTML="";
    if(date == "")
        return
    target = document.querySelector("#available-times-for-"+id);
    target.innerText = "Wait A Moment...."
    $.ajax(
        {
            type : "POST",
            url : "/searchdate",
            data :{
                type : 'dateSearch',
                doctor_id : id,
                date : date,
            },
            success : (data)=>{
                console.log("success");
                target.innerHTML = '';
                console.log(data);
                if(Object.keys(data.available).length){
                    console.log("Available");
                    showDates(target, data.available, id);
                }
                else
                    showFailure(target, id);
            }
        }
    )
}

function showDates(target, available, doc_id){
    head = document.createElement('h3');
    head.innerText = "Select Time";
    target.appendChild(head);
    for(const key in available){
        btn = document.createElement('button');
        btn.classList.add('btn');
        btn.classList.add('btn-primary');
        btn.classList.add('btn-sm');
        btn.classList.add('m-2');
        
        date_full = new Date(available[key]);

        let date = date_full.getDate() + "-" + (date_full.getMonth()+1) + "-" + date_full.getFullYear();
        let time = date_full.getHours() + ":" + date_full.getMinutes();
        
        btn.addEventListener('click', function(){
            showSelectedDateTime(doc_id, date, time);
            
        })
        btn.innerHTML = `
            ${date}<br><b>${time}</b>
        `;
        target.appendChild(btn);
    }

}

function showFailure(target, id){
    div = document.getElementById("date-and-time-for-"+id);
    div.innerHTML="";
    head = document.createElement('h3');
    head.innerText = "Not Available on that particular day !";
    target.appendChild(head);
}


function showSelectedDateTime(id, date, time){
    document.getElementById("paypal-button-container-"+id).innerHTML = "";
    div = document.getElementById("date-and-time-for-"+id);
    div.innerHTML="";
    p = document.createElement('p');
    p.innerHTML = `
        <h4>Selected Date and Time</h4>
        Date: ${date} <br>
        time: ${time} 
    `
    div.appendChild(p);
    document.getElementById('date-for-doctor-'+id).innerText= date;
    document.getElementById('time-for-doctor-'+id).innerText= time;

    document.getElementById('pay-to-proceed-'+id).style.visibility="visible";
    
}