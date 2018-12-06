KindEditor.ready(function(K){
	
	K.create('textarea[name=body]',
		{
		width:'800px',
		height:'200px',
		 designMode:false,
		uploadJson:'/uplaod_file/',
		extraFileUploadParams: {"csrfmiddlewaretoken": $("[name='csrfmiddlewaretoken']").val(),'post_id':window.location.pathname.split('/')[4]},
		filePostName: 'upload_img',
		filterMode: false,
		 
		
		},
	);
	
	
});