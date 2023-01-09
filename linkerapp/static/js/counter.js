
function boxchecked() {

    var displaybox= document.getElementById("Displayedcount");

    var inputs = document.getElementsByTagName("input");
    var inputObj;
    var selectedCount = 0;

    for(var count1 = 0; count1<inputs.length; count1++) {
        inputObj = inputs[count1];

        var type = inputObj.getAttribute("type");

        if (type == 'checkbox' && inputObj.checked) {
            selectedCount++;
        }
    }
       
   if (selectedCount< 0){
    alert(" You haven't selected any workers !");
   }
   else{
    displaybox.value= selectedCount;
    alert("Hey, You selected  " + selectedCount +"  Workers.");
    ;
   }

}



    // var checkBox = document.getElementsByName("selected");
    // var displaybox = document.querySelector('#Displayedcount');

    // count = 0;
    //         for (var i=0; i< checkBox.length; i++) {
    //             if(checkbox[i].checked==0) { checkbox.splice(i,1);}
    //     }
    //     alert("Number of checked checkboxes: "+checkboxes.length);
    // }


     


        // alert(document.querySelectorAll('input[type="checkbox"]:checked').length);

        // function checkboxes(){
        //     var inputElems = document.getElementsByTagName("input"),
        //     count = 0;
        //     for (var i=0; i<inputElems.length; i++) {
        //     if (inputElems[i].type === "checkbox" && inputElems[i].checked === true){
        //         count++;
        //         alert(count);
        //     }
        // }}
        
        

    



// }