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

                <form class='form-horizontal' role='form' method='post'>
                  <div class='form-group'>
                    <label  class='col-sm-2 control-label'
                              for='clue'>Clue</label>
                    <div class='col-sm-10'>
                        <input type='text' class='form-control'
                        id='clue'/>
                    </div>
                  </div>
                  <div class='form-group'>
                    <label class='col-sm-2 control-label'
                          for='cellno' >Cell No</label>
                    <div class='col-sm-10'>
                        <input type='number' class='form-control'
                            id='cellno'/>
                    </div>
                  </div>
                  <div class='form-group'>
                    <label class='col-sm-2 control-label'
                          for='length' >Length</label>
                    <div class='col-sm-10'>
                        <input type='number' class='form-control'
                            id='length'/>
                    </div>
                  </div>
                  <div class='form-group'>
                    <div class='col-sm-offset-2 col-sm-10'>
                      <div class='radio'>
                        <label>
                            <input type='radio' value='1' name='type'/> Across
                        </label>
                      </div>
                      <div class='radio'>
                        <label>
                            <input type='radio' value='0' name='type'/> Down
                        </label>
                      </div>
                    </div>
                  </div>
                  <div class='form-group'>
                    <div class='col-sm-offset-2 col-sm-10'>
                      <button type='submit' class='btn btn-default'>Apply</button>
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
     iDiv.id = ""+i+j;
     iDiv.className = 'cell btn';
     document.getElementById("abc").appendChild(iDiv);

     mod.className = "modal fade";
     mod.id = "m"+i+j;
     document.getElementById("modal_container").appendChild(mod)
     //document.write(i);
     $("#"+i+j).attr('data-target',"#m"+i+j);
     $("#"+i+j).attr('data-toggle',"modal");
     $("#m"+i+j).attr('tabindex',"-1");
     $("#m"+i+j).attr('role',"dialog");

     html = $.parseHTML(str);
     $("#m"+i+j).append(html);

   }
   //document.write("<br>");
   var mybr = document.createElement('br');
   document.getElementById("abc").appendChild(mybr);
   document.getElementById("abc").appendChild(mybr);

}
});
