str =  `<div class='modal-dialog'>
        <div class='modal-content'>
            <!-- Modal Header -->
            <div class='modal-header'>
                <button type='button' class='close'
                   data-dismiss='modal'>
                       <span aria-hidden='true'>&times;</span>
                       <span class='sr-only'>Close</span>
                </button>
                <h4 class='modal-title' id='myModalLabel'>
                    Clue Info
                </h4>
            </div>

            <!-- Modal Body -->
            <div class='modal-body'>

                <form class='form-horizontal comp' role='form' action='/clue' method='post'>
                  <input class="hidden" type="hidden" name="cell_num" value="0">
                  <div class='form-group'>
                    <label  class='col-sm-2 control-label'
                              for='clue'>Clue</label>
                    <div class='col-sm-10'>
                        <input type='text' name='clue' class='form-control'
                        id='clue' required/>
                    </div>
                  </div>
                  <div class='form-group'>
                    <label class='col-sm-2 control-label'
                          for='clueno' >Clue No</label>
                    <div class='col-sm-10'>
                        <input type='number' min=1 step=1 name='clueno' class='form-control clue1'
                            id='clueno' required />
                    </div>
                  </div>
                  <div class='form-group'>
                    <label class='col-sm-2 control-label'
                          for='length' >Length</label>
                    <div class='col-sm-10'>
                        <input id='clue_len' min=1 type='number' step=1 name='length' class='form-control textbox'
                            required/>
                    </div>
                  </div>
                  <div class='form-group'>
                    <div class='col-sm-offset-2 col-sm-10'>
                      <div class='radio'>
                        <label>
                            <input class="across-radio" type='radio' value='1' name='type' required/> Across
                        </label>
                      </div>
                      <div class='radio'>
                        <label>
                            <input class="down-radio" type='radio' value='0' name='type'/> Down
                        </label>
                      </div>
                    </div>
                  </div>
                  <div class='form-group'>
                    <div class='col-sm-offset-2 col-sm-10'>
                      <div class='radio'>
                        <label>
                            <input type='radio' value='2' name='answer_type' required/> Verb
                        </label>
                      </div>
                      <div class='radio'>
                        <label>
                            <input type='radio' value='1' name='answer_type'/> Noun
                        </label>
                      </div>
                      <div class='radio'>
                        <label>
                            <input type='radio' value='0' name='answer_type'/> No Idea
                        </label>
                      </div>
                    </div>
                  </div>
                  <div class='form-group'>
                    <div class='col-sm-offset-2 col-sm-10'>
                      <button type='submit' class='btn btn-default last-hur' id='submit_button'>Apply</button>
                    </div>
                  </div>
                </form>
            </div>
        </div>
    </div>`;

$(document).ready(function() {
  var iDiv,mod;
  var i,j;
  var dow=localStorage.getItem("dow");
  var acr=localStorage.getItem("acr");
  var acr_key=localStorage.getItem("acr_key");
  var dow_key=localStorage.getItem("dow_key");
  acr+=".";
  dow+="."
  acr_key+=".";
  dow_key+=".";
  localStorage.setItem("acr",acr);
  localStorage.setItem("acr_key",acr_key);
  localStorage.setItem("dow_key",dow_key);
  localStorage.setItem("dow",dow);
  //document.write("<br>");
  for(i=0;i<16;i++)
  {
    for(j=0;j<16;j++){
     iDiv = document.createElement('div');
     mod = document.createElement('div');
     numDiv = document.createElement('div');
     k = i*100 + j
     iDiv.id = ""+k;
     iDiv.className = 'cell';
     document.getElementById("abc").appendChild(iDiv);

     numDiv.id="n"+k;
     numDiv.className='cellNo';
     iDiv.appendChild(numDiv);

     mod.className = "modal fade";
     mod.id = "m"+k;
     document.getElementById("modal_container").appendChild(mod)
     //document.write(i);
     $("#"+k).attr('data-target',"#m"+k);
     $("#"+k).attr('data-toggle',"modal");
     $("#m"+k).attr('tabindex',"-1");
     $("#m"+k).attr('role',"dialog");

     html = $.parseHTML(str);
     var $html=$(html);

 (function(myk){

      var yo=$.parseHTML("<div class='isa_error'><i class='fa fa-times-circle'></i>Clue length is out of bounds.</div>");
      var yo1=$.parseHTML("<div class='isa_error cluenum'><i class='fa fa-times-circle'></i>Identical clue already exists.</div>");
      var yo2=$.parseHTML("<div class='isa_error cluenum1'><i class='fa fa-times-circle'></i>Clue overlaps with existing clue.</div>");
      var selection = undefined;
      var ACROSS = 1;
      var DOWN = 2;

      function show_err(){

        $(".in").find("input.textbox").parent().append(yo);
        $(':input[type="submit"]').prop('disabled', true);

      }
      function show_err1(){

        $(".in").find("input.textbox").parent().append(yo1);
        $(':input[type="submit"]').prop('disabled', true);

      }

      function show_err2(){

        $(".in").find("input.textbox").parent().append(yo2);
        $(':input[type="submit"]').prop('disabled', true);

      }

      function hide_err(){
        $(".in").find(".isa_error").remove();
        $(':input[type="submit"]').prop('disabled', false);
      }
      function hide_err1(){
        $(".in").find(".cluenum").remove();
        $(':input[type="submit"]').prop('disabled', false);
      }
        function hide_err2(){
        $(".in").find(".cluenum1").remove();
        $(':input[type="submit"]').prop('disabled', false);
      }

      function checkAcross(){
        var len = $(".in").find("input.textbox").val();
        if(myk%100 + Number(len) > 16){
                show_err();  
        }
        else{
                hide_err();
        }
      }
      
      function checkAcrossClue(){
        console.log("called checacrossclue");
        var clu = $(".in").find("input.clue1").val();
              acr=localStorage.getItem("acr");
              if (acr.indexOf("."+clu+".") >= 0){
                show_err1();

              }
              else{
                hide_err1();

            }
      } 

      function checkAcrossKey(){
        var len = $(".in").find("input.textbox").val();
              acr_key=localStorage.getItem("acr_key");
              var g=0;
              while(g<len)
              {
              if (acr_key.indexOf("."+(Number(myk)+g)+".") >= 0){
                show_err2();
                break;

              }
              else{
                hide_err2();
              }
              g++;
            }
      }

      function checkDownKey(){
        console.log("called checkdownkey");
        var len = $(".in").find("input.textbox").val();
        dow_key=localStorage.getItem("dow_key");
              var g=0;
              console.log(len+"  "+dow_key+"  "+myk);
              while(g<len)
              {
                console.log(Number(myk)+g);
              if (dow_key.indexOf("."+(Number(myk)+g*100)+".") >= 0){
                show_err2();
                break;

              }
              else{
                hide_err2();
              }
              g++;
            }
      }

      function setDownKey(){
        var len = $(".in").find("input.textbox").val();
              dow_key=localStorage.getItem("dow_key");
              var g=0;
              while(g<len)
              {
              if (dow_key.indexOf("."+(Number(myk)+g*100)+".") >= 0){

              }
              else{
                dow_key+=((Number(myk)+g*100)+".");
              localStorage.setItem("dow_key",dow_key);
              }
              g++;
            }
      }
      function setAcrossKey(){
        var len = $(".in").find("input.textbox").val();
              acr_key=localStorage.getItem("acr_key");
              var g=0;
              while(g<len)
              {
              if (acr_key.indexOf("."+(Number(myk)+g)+".") >= 0){

              }
              else{
                acr_key+=((Number(myk)+g)+".");
              localStorage.setItem("acr_key",acr_key);
              }
              g++;
            }
      }
      function setAcrossClue(){
        var clu = $(".in").find("input.clue1").val();
              acr=localStorage.getItem("acr");
              if (acr.indexOf("."+clu+".") >= 0){

              }
              else{
              acr+=(clu+".");
              localStorage.setItem("acr",acr);
            }
      }
      function checkDownClue(){
        var clu = $(".in").find("input.clue1").val();
              dow=localStorage.getItem("dow");
              if (dow.indexOf("."+clu+".") >= 0){
                show_err1();

              }
              else{
                hide_err1();
            }
      }

      function setDownClue(){
        var clu = $(".in").find("input.clue1").val();
              dow=localStorage.getItem("dow");
              if (dow.indexOf("."+clu+".") >= 0){

              }
              else{
              dow+=(clu+".");
              localStorage.setItem("dow",dow);
            }
      }

      function checkDown(){
         var len = $(".in").find("input.textbox").val();
         //console.log(`down checking len ${len} n ${myk}`)
           if(Math.trunc(myk/100) +Number(len) > 16){
               show_err();  
           }
           else{
              hide_err();
           }
      }



        $html.find("input.textbox").change(function(){
          console.log("On Change for "+selection);
          //error check
          switch(selection){
            case undefined: return;break;
            case ACROSS : checkAcross();checkAcrossKey();break;
            case DOWN: checkDown();checkDownKey();break;
          }

        });

        $html.find("input.clue1").change(function(){
          //error check
          switch(selection){
            case undefined: return;break;
            case ACROSS : checkAcrossClue();break;
            case DOWN: checkDownClue();break;
          }

        });
        $html.find("form.comp").submit(function(){
          //error check
          switch(selection){
            case undefined: return;break;
            case ACROSS : setAcrossClue();setAcrossKey();break;
            case DOWN: setDownClue();setDownKey();break;
          }

        });

        $html.find('.across-radio').click(function () {
              selection = ACROSS;
              checkAcross();
              checkAcrossClue();
              checkAcrossKey();

              console.log(acr);console.log(acr_key);

        });
      

      $html.find('.down-radio').click(function () {
          selection = DOWN;
          checkDown();
          checkDownClue();
          console.log("checkDownkey to call");
          checkDownKey();
          console.log(dow);console.log(dow_key);

         
        });
      })(k);

     $("#m"+k).append(html);
     u = $("#m"+k+' input.hidden');
     u.val(k);


     //document.write(u.val());
     //.val(''+k);
     //v = u.getElementByTagName("div");
     // a = v.getElementByTagName("div")[0];
     // b = a.getElementByTagName("div")[1];
     // c = b.getElementByTagName("form")[0];
     // w.attr('value',k);

   }
   //document.write("<br>");
   var mybr = document.createElement('br');
   document.getElementById("abc").appendChild(mybr);
   document.getElementById("abc").appendChild(mybr);


}
});
