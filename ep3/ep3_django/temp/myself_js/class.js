function showModal(){
    document.getElementById('shadow').classList.remove('myself-hide')
    document.getElementById('modal').classList.remove('myself-hide')
}
$('#cancle_add_class').click(function(){
    $("#shadow,#modal").addClass("myself-hide")
})
function cancleModal(){
    document.getElementById("shadow-edit").classList.add('myself-hide')
    document.getElementById('modal-edit').classList.add('myself-hide')
}
function AjaxSend(){
    $.ajax({
        url:'/modal_add_class/',
        type:'POST',
        data:{
            'title':$('#title').val()
        },
        success:function(data){
            //当服务端处理完成后，返回数据时，该函数自动调用
            //data代表服务端返回的值
            //服务器先拿到值
            if (data =="ok"){
                location.href='/class/';
            }else{
                $('#error').text(data);
            }

        }
    })
}
function AjaxDelete(obj){
    var class_id =obj.getAttribute("value")
    $.ajax({
        url:'/modal_del_class/',
        type:'POST',
        data:{
            'class_id':class_id
        },
        success:function(data){
            if (data =='200'){
                location.href ='/class/'
            }else{
                alert('error delete class id :'+class_id)
            }
        }
    })
}
function AjaxEdit(obj){
    var class_id =obj.getAttribute("value")
    $.ajax({
        url:'/modal_edit_class/',
        type:'GET',
        data:{
            'nid':class_id
        },
        success:function(data){
            if (data !=''){
                document.getElementById('shadow-edit').classList.remove('myself-hide')
                document.getElementById('modal-edit').classList.remove('myself-hide')
                $('#s_c_id').text(class_id)
                $('#s_c_name').text(data)
            }else{
                alert('error edit id of class:'+class_id)
            }

        }
    })
}
function edit_send(){
    var class_id =$('#s_c_id').text();
    var new_classname =$('#class_input').val();
    $.ajax({
        url:'/modal_edit_class/',
        type:'POST',
        data:{
            'class_id':class_id,
            'new_c_name':new_classname,
        },
        success:function(data){
            if(data != 'ERROR'){
                location.href ='/class/'
            }else{
                alert('error edit for class:'+class_id)
            }
        }
    })
}
