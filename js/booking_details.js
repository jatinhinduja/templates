var apiUrl = "https://p4bkuyvb1h.execute-api.ap-south-1.amazonaws.com/dev/booking_details";

fetch(apiUrl)
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    var result = [];
    var s = data.body;
    console.log(data.body);
    const myJSON = JSON.stringify(data.body);
    document.getElementById("demo").innerHTML = myJSON;
  })
  .catch((err) => {
    console.log(err);
  });
1;