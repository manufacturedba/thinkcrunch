{% load staticfiles %}
$(document).ready(function() {
  document.domain = "thinkcrunch.com";
  $("#id_content").wymeditor({
	  skin: "django", lang: "{{ lang }}",
	  stylesheet: "{% static "zinnia/css/wymeditor_styles.css" %}",
	  updateSelector: "input:submit", updateEvent: "click",
	  postInit: function(wym) {
	      wym.hovertools();
	  }
      });
    });
