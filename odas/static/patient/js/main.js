console.log("Main.js working");

function dateForAppointment(id){
    date = document.querySelector('#app-date-for-'+id).value;

    document.getElementById("paypal-button-container-"+id).innerHTML = "";
    // document.getElementById('pay-to-proceed-'+id).style.visibility="hidden";
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
        let time_formatted = date_full.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true })

        btn.addEventListener('click', function(){
            showSelectedDateTime(doc_id, date, time, time_formatted);
            
        })
        btn.innerHTML = `
            ${date}<br><b>${time_formatted}</b>
        `;
        target.appendChild(btn);
    }

}

function showFailure(target, id){
    div = document.getElementById("date-and-time-for-"+id);
    div.innerHTML="";
    head = document.createElement('h3');
    head.classList.add("text-danger");
    head.innerHTML = `<i class="bi bi-emoji-frown"></i><br>Not Available on this day!`;
    target.appendChild(head);
}


function showSelectedDateTime(id, date, time, time_formatted){
    document.getElementById("paypal-button-container-"+id).innerHTML = "";
    let div = document.getElementById("date-and-time-for-"+id);
    div.innerHTML="";

    let charge = document.getElementById("charge-for-doctor-"+id).innerHTML;
    let paypal = document.getElementById("paypal-for-doctor-"+id).innerHTML;
    
    div.classList.add("d-flex");
    div.classList.add("justify-content-center");
    div.innerHTML = `
    <div class="card border-primary" style="width: 20rem;" id="payment-handler-for-${id}">
        <div class="card-header bg-primary text-white">
            <h5 class="card-title text-center">Selected date and Time</h5>
        </div>

        <div class="card-body">
            <ul class="list-group list-group-flush">
                <li class="list-group-item text-primary"><i class="bi bi-calendar2-event"></i> <b> ${date}</b></li>
                <li class="list-group-item text-primary"><i class="bi bi-clock"></i><b> ${time_formatted}</b></li>
                <li class="list-group-item">Total Amt. payble: <b>$${charge}</b></li>
            </ul>
            <div class="card-footer text-center">
                <button onclick= \"showPayment('${charge}','${paypal}','${id}','${date}','${time}')\" class="btn btn-outline-success" id="pay-to-proceed-{{doctor.id}}">Proceed to Payment</button>
            </div>
        </div>
    </div>
    `
    document.getElementById("payment-handler-for-"+id).scrollIntoView();

    // document.getElementById('pay-to-proceed-'+id).style.visibility="visible";
    
}