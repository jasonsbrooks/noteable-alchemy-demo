$(document).ready(function() {
	$('#alchemy-text').ajaxForm({
		success: function(html, status, xhr, myForm) {
			var taxonomy = html.taxonomy.taxonomy;
			var taxonomyHTML = '<p><b>Taxonomy (General Topic):</b></p>'
			var concepts = html.concepts.concepts;
			var conceptsHTML = '<p><b>Concepts in Notes:</b></p>'
			$.each(taxonomy, function( index, value ) {
			  taxonomyHTML += '<p>' + value.label + ': ' + value.score + '</p>'
			});
			$.each(concepts, function( index, value ) {
			  conceptsHTML += '<p>' + value.text + ': ' + value.relevance + '</p>'
			});
			$('#taxonomy').html(taxonomyHTML);
			$('#concepts').html(conceptsHTML);
		}
	}); 
});