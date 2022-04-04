const confirmDoctorEdit = ()=>{
    const form = document.querySelector('#edit-form');
    form.submit();
}

const fetchPatientReports = (id) =>{

    $.ajax({
        url : `${document.location.origin}/reports/patient/${id}`,
        data : "json",
        method : "GET",

        success : (data) =>{
            showReportsModal(data);
        }
    });
}

const showReportsModal = (data)=> {
    var trigger = null;
    try {
        trigger= document.getElementById('report-modal-open-button');
        if(trigger === null)
            throw new Error();
    }
     catch(exception){  
        trigger = document.createElement('button');
        trigger.setAttribute('type',"button");
        trigger.setAttribute('id',"report-modal-open-button");
        trigger.setAttribute('data-bs-toggle',"modal");
        trigger.setAttribute('data-bs-target',"#reports-modal");
        trigger.style.display="none";
        document.body.appendChild(trigger);
    }
    finally {

        const reports = data.map(report=> `
        <div>
        <b>${report.name}</b>
        <a href=${document.location.origin+`/edit/patient/reports/${report.id}`} target="_blank">View this Report</a>
        </div>
        `);




        var modalContainer = document.getElementById('report-modal-content');
        modalContainer.innerHTML =
        `
        <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Reports</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
            ${reports}
        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        </div>
        
        `

        trigger.click();
    }

}