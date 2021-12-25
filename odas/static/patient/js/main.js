console.log("Main.js working");

function dateForAppointment(id){
    date = document.querySelector('#app-date-for-'+id).value;
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
                    showDates(target, data.available);
                }
                else
                    showFailure(target);
            }
        }
    )
}

function showDates(target, available){
    head = document.createElement('h3');
    head.innerText = "Select Time";
    target.appendChild(head);
    for(const key in available){
        btn = document.createElement('button');
        btn.classList.add('btn');
        btn.classList.add('btn-primary');
        btn.classList.add('btn-sm');
        btn.classList.add('m-2');
        btn.innerText = `
            ${available[key]}
        `;
        target.appendChild(btn);
    }

}

function showFailure(target){
    head = document.createElement('h3');
    head.innerText = "Not Available on that particular day !";
    target.appendChild(head);
}