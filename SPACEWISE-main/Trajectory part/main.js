const displayLocation = document.querySelector("#location");
const apiRoot = "https://sscweb.sci.gsfc.nasa.gov/WS/sscr/2";
const satellites = document.querySelector("#satellites");

updateLocation();
fetch(apiRoot + "/spaseObservatories", {headers: {'Accept': 'application/json'}})
.then(res => res.json())
.then(satellite => {
	satellite = satellite.Observatory[1];
	satellite.forEach(satellite => {
		const li = document.createElement("li");
		li.textContent = satellite.Name;
		satellites.appendChild(li);
		fetch(apiRoot + "/locations/" + satellite.Id + "/20190101T000000Z,20190101T001000Z/",
		{headers: {'Accept': 'application/json'}})
		.then(res => res.json())
		.then(satelliteData => {
			const coordinateData = satelliteData.Result.Data[1][0].Coordinates[1][0];
			console.log(coordinateData);
			li.textContent += "Longitude: " + coordinateData.Longitude[1][0];
			li.textContent += "Latitude: " + coordinateData.Latitude[1][0];
		});
	});
})


function updateLocation() {
	if (navigator.geolocation)
		setInterval(() => navigator.geolocation.getCurrentPosition(location => {
			displayLocation.textContent = `${location.coords.latitude}, ${location.coords.longitude}`;
		}), 250);
	else
		displayLocation.textContent = "You need to give this website permission to use your GPS"
}