var apiUrl = "https://p4bkuyvb1h.execute-api.ap-south-1.amazonaws.com/dev/home/booking_details";

fetch(apiUrl)
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    var result = [];
    var s = data.body;
    console.log(data.body);
    var myObject = eval("(" + s + ")");
    for (i in myObject) {
      result.push({
        room_id: myObject[i]["room_id"],
        price: myObject[i]["price"],
        room_type: myObject[i]["room_type"],
      });
    }
    console.log(result);
    document.getElementById("demo").innerHTML = data.body;
  })
  .catch((err) => {
    console.log(err);
  });
l;