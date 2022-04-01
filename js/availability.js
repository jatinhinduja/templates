var apiUrl = "https://p4bkuyvb1h.execute-api.ap-south-1.amazonaws.com/dev/admin";

fetch(apiUrl).then((response) => {
    return response.json();
  })
  .then((data) => {
    var result = [];
    var s = data.body;
    console.log(data.body);
    var myObject = eval("(" + s + ")");
    for (i in myObject) {
      result.push({
        date: myObject[i]["date"],
        room_101: myObject[i]["101"],
        room_102: myObject[i]["102"],
        room_103: myObject[i]["103"],
        room_104: myObject[i]["104"],
        room_105: myObject[i]["105"],
        room_201: myObject[i]["201"],
        room_202: myObject[i]["202"],
        room_203: myObject[i]["203"],
        room_204: myObject[i]["204"],
        room_205: myObject[i]["205"]
      });
    }
    console.log(result);
    document.getElementById("check").innerHTML = data.body;
  })
  .catch((err) => {
    console.log(err);
  });
l;
