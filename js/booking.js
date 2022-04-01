jQuery("https://p4bkuyvb1h.execute-api.ap-south-1.amazonaws.com/dev/booking").submit(function(e){
    //The following stops the form from redirecting
    e.preventDefault();
    jQuery("https://p4bkuyvb1h.execute-api.ap-south-1.amazonaws.com/dev/booking").ajaxSubmit({
        type: 'POST',
        url: jQuery('https://p4bkuyvb1h.execute-api.ap-south-1.amazonaws.com/dev/booking').attr('action'),
        data: jQuery('https://p4bkuyvb1h.execute-api.ap-south-1.amazonaws.com/dev/booking').serialize(),
        success: function (data) {
            //The data variable will contain the response data
            //if it's successful, you can no redirect wherever you want
            window.location.href = "booking.html";
        }
    });
});
