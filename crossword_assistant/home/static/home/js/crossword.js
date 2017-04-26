$(document).ready(function() {
  var iDiv,mod;
  var i,j;

  //document.write("<br>");
  for(i=0;i<16;i++)
  {
    for(j=0;j<16;j++){
     iDiv = document.createElement('div');
     //mod = document.createElement('div');
     numDiv = document.createElement('div');
     textDiv=document.createElement('div')
     k = i*100 + j
     iDiv.id = ""+k;
     iDiv.className = 'cell';
     document.getElementById("abc").appendChild(iDiv);


     numDiv.id="n"+k;
     textDiv.id="t"+k;
     textDiv.className='textDiv'
     numDiv.className='cellNo';
     iDiv.appendChild(numDiv);
     iDiv.appendChild(textDiv);


   }
   //document.write("<br>");
   var mybr = document.createElement('br');
   document.getElementById("abc").appendChild(mybr);
   document.getElementById("abc").appendChild(mybr);

}
});
