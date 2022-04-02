console.log("FAHFHAJHFAJFH");
    function logSubmit(event) {
        var form = document.querySelector('form');
        var formData = new FormData(form);
    console.log("HERE");
    var object = {};
    formData.forEach(function(value, key){
        object[key] = value;
        });
    var json = JSON.stringify(object);
    console.log(json);
    $.ajax({
        type: "POST",
        url: "https://p4bkuyvb1h.execute-api.ap-south-1.amazonaws.com/dev/booking",
        data: json,
        contentType: "application/json",
        success: function (result) {
          console.log(result);
        },
        error: function (result, status) {
          console.log(result);
        }
      });
    event.preventDefault();
    }

    var form = document.querySelector('form');
    form.addEventListener('submit', logSubmit);