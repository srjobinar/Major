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

                <form class='form-horizontal' role='form' action='/clue' method='post'>
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
                        <input type='number' min=1 step=1 name='clueno' class='form-control'
                            id='clueno' required />
                    </div>
                  </div>
                  <div class='form-group'>
                    <label class='col-sm-2 control-label'
                          for='length' >Length</label>
                    <div class='col-sm-10'>
                        <input id='clue_len' type='number' cln=1 step=1 name='length' class='form-control textbox'
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
                      <button type='submit' class='btn btn-default' id='submit_button'>Apply</button>
                    </div>
                  </div>
                </form>
            </div>
        </div>
    </div>`;

$(document).ready(function() {
  var iDiv,mod;
  var i,j;

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
      var selection = undefined;
      var ACROSS = 1;
      var DOWN = 2;

      function show_err(){

        $(".in").find("input.textbox").parent().append(yo);
        $(':input[type="submit"]').prop('disabled', true);

      }

      function hide_err(){
        $(".in").find(".isa_error").remove();
        $(':input[type="submit"]').prop('disabled', false);
      }

      function checkAccross(){
        var len = $(".in").find("input.textbox").val();
        if(myk%100 + Number(len) > 16){
                show_err();  
        }
        else{
                hide_err();
        }
      }

      function checkDown(){
         var len = $(".in").find("input.textbox").val();
         console.log(`down checking len ${len} n ${myk}`)
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
            case ACROSS : checkAccross();break;
            case DOWN: checkDown();break;
          }

        });

        $html.find('.across-radio').click(function () {
              selection = ACROSS;
              checkAccross();
        });
      

      $html.find('.down-radio').click(function () {
          selection = DOWN;
          checkDown();
         
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
