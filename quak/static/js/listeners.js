$(function() {
  $('.voteIncrement').click(function() {
    var question_guid = $(this).find('#question_guid').val();
    var number = $(this).parent().find('.number');
    $.ajax({
        type: 'GET'
      , url: '/quakapp/incrementVote?guid=' + question_guid
    }).done(function(data) {
      number.html(parseInt(number.html()) + 1);
    }).fail(function() {
      alert('Sorry! Something went wrong.')
    });
  })
})

$(function() {
  $('#createQuestion').submit(function(event) {
    /*event.preventDefault();
    console.log('got here');
    // use the same model to create a new question
    var question_title = $(this).find('question_title');
    var presentation_guid = $('#presentation_guid').val();
    $.ajax({
        type: 'POST'
      , url: '/quakapp/newQuestion/'
      , data: {
            'title': question_title
          , 'presentation_guid': presentation_guid
        }
    }).done(function() {
      alert('Question posted!')
    }).fail(function() {
      alert("Sorry! Something went wrong. Please try again in a few moments.");
    })*/
  })
})