var options = {
  enableHighAccuracy: true,
  timeout: 5000,
  maximumAge: 0
};

function success(pos) {
  var crd = pos.coords;

  console.log('Your current position is:');
  console.log(`Latitude : ${crd.latitude}`);
  console.log(`Longitude: ${crd.longitude}`);
  console.log(`More or less ${crd.accuracy} meters.`);
};

function error(err) {
  console.warn(`ERROR(${err.code}): ${err.message}`);
};

navigator.geolocation.getCurrentPosition(success, error, options);

require(["dijit/form/Button",
					"dojo/dom",
          "dojo/domReady!"],
          
          function(Button, dom){
          var myButton = new Button({
          label: "get location",
          onClick: function(){
          	dom.byId("location").innerHTML = "Location in console";
            navigator.geolocation.getCurrentPosition(success, error, options);
          }
          }, "progButtonNode").startup();
          })