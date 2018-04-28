

 jQuery.getJSON("http://localhost:5000/api/tweets", function(data) {
   var rows=data.length;
   var k = 0;
//var table_body = '<table border="1" id="example"><tbody>';
var table_body ='<dl>';
for(i =0;i<data.length;i++){
 var myString = data[i]["date"];
 var newString = myString.substr(0, myString.length-3);
     table_body+='<dt>';

     table_body +='<dd id="list1"><b>';
     table_body +=data[i]["tweet"];
     table_body +='</dd></b>';

     table_body +='<dd id="list2"><i>';
     table_body +='By: '+ data[i]["user"];
     table_body +=' '+'('+ newString+')';
     table_body +='</dd></i>';

     /*table_body +='<dd>';
     table_body +=data[i]["user"];
     table_body +='</dd>';*/
     table_body+='</dt>';
}

 //table_body+='</tbody></table>';
 table_body+='</dl>'
$('#style-2').html(table_body);
   console.log(data);
 });
