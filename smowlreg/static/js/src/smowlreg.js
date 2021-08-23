/* Javascript for SMOWLREG*/
function SmowlRegXBlock(runtime, element, settings) {
    $(function ($) {
        if (settings.has_settings){
            var url2 = window.location.href;
            var url = url2.split("+").join("%252B");
            var courseID = settings.course_id;
            var userID = settings.user_id;
            var link = settings.controllerReg_link;
            var iduser = "&user_idUser="+userID;
            var coursecontainer = "&course_Container="+courseID;
            var link2 = "&Course_link="+url;
            var url4 = link+iduser;
            var url5 = url4+coursecontainer;
            var url6 = url5 + link2;
            var decoded = url6.replace(/&amp;/g, '&');
            $(element).find('#urlFinal2')[0].href =decoded;
            //document.getElementById("urlFinal2").href =decoded;
        }
    });
}
