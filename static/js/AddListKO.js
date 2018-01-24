
ko.validation.init({
    registerExtenders: true,
    messagesOnModified: true,
    insertMessages: true,
    parseInputAttributes: true,
    errorClass: 'errorStyle',
    messageTemplate: null
}, true);

function ReqDetails() {
	var clientData;
    $.ajax({
        type: 'GET',
        url: '/features/clients/',
        contentType: "application/javascript",
        dataType: "json",
        async:false,
		beforeSend: function(request) {
					request.setRequestHeader("Authorization", 'JWT '+ window.sessionStorage.accessToken);
		},
        success: function (data) {
            clientData = data;
        },
        error: function (jq, st, error) {
			if(error=="Unauthorized"){
				window.location.href = "/"
			}
        }
    });
	var productData;
    $.ajax({
        type: 'GET',
        url: '/features/products/',
        contentType: "application/javascript",
        dataType: "json",
        async:false,
		beforeSend: function(request) {
					request.setRequestHeader("Authorization", 'JWT '+ window.sessionStorage.accessToken);
		},
        success: function (data) {
            productData = data;
        },
        error: function (jq, st, error) {
            if(error=="Unauthorized"){
				window.location.href = "/"
			}
        }
    });
    var that = this;
    that.validateNow = ko.observable(false);
    that.feature_title = ko.observable().extend({ required: true });
    that.feature_desc = ko.observable().extend({ required: true });
	that.priority = ko.observable().extend({ required: true, min:1, max:99999999 });
    that.client_name = ko.observableArray(clientData);
    that.client_id = ko.observable().extend({ required: true });
    that.target_date = ko.observable().extend({
							required: true, 
							validation: {
								validator: function (val) {
									val = val.replace(/-/g,'/')
									return new Date(val) > new Date();
								},
								message: "Target date should be greater than today's date",
							}
						});
    that.product_area = ko.observableArray(productData);
    that.product_id = ko.observable().extend({ required: true });
    that.errors = ko.validation.group(that);
}

function RequisiteDetailsVM() {
    var that = this;
    that.ReqDetails = new ReqDetails(); 
    that.reset = function () {
        window.location.href="/featurescreen"
    };
    that.submit = function () {
        that.ReqDetails.validateNow(true);
        if (that.ReqDetails.errors().length === 0) {
            var json1 = ko.toJSON(that.ReqDetails);
            $.ajax({
                url: '/features/add',
                type: 'POST',
                dataType: 'json',
                data: json1,
                contentType: 'application/json; charset=utf-8',
				beforeSend: function(request) {
					request.setRequestHeader("Authorization", 'JWT '+ window.sessionStorage.accessToken);
				},
                success: function (data) {
                    var message = data.Message;
                    window.location.href = "/featurescreen";
                },
				error: function (jq, st, error){
					if(error=="Unauthorized"){
						window.location.href = "/"
					}
				}
            });
        }
        else {
            that.ReqDetails.errors.showAllMessages();
            return;
        }
    };
};
var _vm = new RequisiteDetailsVM();
$(function () {
    ko.applyBindings(_vm);
});

