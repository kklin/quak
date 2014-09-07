$(function() {
  $('.voteIncrement').click(function() {
    var question_guid = $(this).parent().find('question_guid').val();
    $.ajax({
        type: 'GET'
      , url: '/quakapp/incrementVote?guid=' + question_guid
    }).done(function(data) {
      if (data === 'success') {
        // here update the count on the page
        console.log('Vote for ' + question_guid + ' updated');
      } else if (data === 'error') {
        // here say something went wrong
        alert("Sorry, something went wrong! Try again in a few seconds.")
      } else {
        // should never be called
        console.log("Not finding the right content");
      }
    }).fail(function() {
      alert('Sorry! Something went wrong.')
    });
  })
})

$(function() {
  $('#newQuestion').submit(function() {
    // use the same model to create a new question
    var question_text = $(this).find('question_text');
    $.ajax({
        type: 'POST'
      , url: '/quakapp/newQuestion/'
      , data: {
          'title': question_text
        }
    }).done(function() {
      // refresh the page?
      // or just input the new question on the page
      alert('Question posted!')
      window.location = window.location.href;
    }).fail(function() {
      alert("Sorry! Something went wrong. Please try again in a few moments.")''
    })
  })
})