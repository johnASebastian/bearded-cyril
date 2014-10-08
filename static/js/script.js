'use strict';

(function() {
	var zones = document.querySelectorAll('div.zone');

	var Zone = function(element) {
		var zone = this;
		console.log('zone', element, element.dataset);
		zone.data = element.dataset;
		zone.element = element;

		this.startClicked = function(event, b, c) {
			var xhr = new XMLHttpRequest();
			xhr.open('POST', '/zones/'+zone.data.zoneId+'/on', true); // on off delay(duration={mins})
			xhr.onload = function(e) {
				if (this.status == 200) {
					console.log('success');
					// Note: .response instead of .responseText
					// var blob = new Blob([this.response], {type: 'image/png'});
				}
			};
			xhr.send();
		};
		this.cancelClicked = function(event) {
			var xhr = new XMLHttpRequest();
			xhr.open('POST', '/zones/'+zone.data.zoneId+'/off', true); // on off delay(duration={mins})
			xhr.onload = function(e) {
				if (this.status == 200) {
					console.log('success');
					// Note: .response instead of .responseText
					// var blob = new Blob([this.response], {type: 'image/png'});
				}
			};
			xhr.send();
		};
		this.postponeClicked = function(event) {
			var xhr = new XMLHttpRequest();
			xhr.open('POST', '/zones/'+zone.data.zoneId+'/delay?duration=5', true); // on off delay(duration={mins})
			xhr.onload = function(e) {
				if (this.status == 200) {
					console.log('success');
					// Note: .response instead of .responseText
					// var blob = new Blob([this.response], {type: 'image/png'});
				}
			};
			xhr.send();
		};

		var startButton = element.querySelector('button.start');
		startButton.addEventListener('click', this.startClicked);
		var cancelButton = element.querySelector('button.cancel');
		cancelButton.addEventListener('click', this.cancelClicked);
		var postponeButton = element.querySelector('button.postpone');
		postponeButton.addEventListener('click', this.postponeClicked);
	};

	for (var i=0,l=zones.length; i<l; i++) {
		console.log('loop');
		var zone = new Zone(zones[i]);
	}

})();
