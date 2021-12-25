
var showPayment=(charge, paypal_acc,id)=>{
    var date = document.getElementById('date-for-doctor-'+id).innerHTML;
    var time = document.getElementById('time-for-doctor-'+id).innerHTML;
    console.log("Date is ",date);
    console.log(charge, paypal_acc, id, date, time);
    paypal.Buttons({
        style: {
            color:  'blue',
            shape:  'pill',
            label:  'pay',
            height: 40
        },
        // Set up the transaction
        createOrder: function(data, actions) {
            return actions.order.create({
                purchase_units: [{
                    amount: {
                        value: parseFloat(charge),
                    },
                    payee : {
                        email_address : paypal_acc,
                    }
                }]
            });
        },

        // Finalize the transaction
        onApprove: function(data, actions) {
            return actions.order.capture().then(function(orderData) {
                // Successful capture! For demo purposes:
                //console.log('Capture result', orderData, JSON.stringify(orderData, null, 2));
                var transaction = orderData.purchase_units[0].payments.captures[0];
                //alert('Transaction '+ transaction.status + ': ' + transaction.id + '\n\nSee console for all available details');
                

                if(transaction.status === "COMPLETED"){
                    a = document.querySelector('#successful-payment-'+id);
                    a.href = "/makeappointment/"+id+"/"+date +"/"+time+"/";
                    a.click();
                    alert("Payment Done!");
                }
                else{
                    
                    console.log("payment Failed");
                }
                
                // Replace the above to show a success message within this page, e.g.
                // const element = document.getElementById('paypal-button-container');
                // element.innerHTML = '';
                // element.innerHTML = '<h3>Thank you for your payment!</h3>';
                // Or go to another URL:  actions.redirect('thank_you.html');
            });
        }


    }).render('#paypal-button-container-'+id);

}