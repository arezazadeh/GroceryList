function urlify(text) {
    let urlRegex = /(https?:\/\/[^\s]+)/g;
    return text.replace(urlRegex, function (url) {
      return '<a href="' + url + '" target="_blank">' + " Link to the site" + '</a>';
    })
  }

  let post = document.getElementById('dish').innerHTML;
  let postHtml = urlify(post);
  document.getElementById('dish').innerHTML = postHtml

function user_mention(post){
  const userRegex = /@\b(\w*\w*)\b/g;
  return post.replace(userRegex, function (username) {
      return '<a href="">' + `${username}` + '</a>';
  })
}

const user_name = document.getElementById('dish').innerHTML;



function user_mention_api_call(text){

  const userRegex = /@\b(\w*\w*)\b/g;
  const testing = userRegex.test(text)
  console.log(testing)
  const a = text.match(userRegex)
  console.log(a.length)
  if (a !== null) {
      if (a.length === 1 ) {
          const user_mentioned = a[0].split('@')[1]
          fetch(`/grocery/api/user/${user_mentioned}`).then(response => response.json())
          .then(function (data) {
              console.log(data.user_list)
              if (data.user_list.length !== 0) {
                  const user_name = document.getElementById('dish').innerHTML;
                  const user_mention_txt = user_mention(user_name);
                  document.getElementById('dish').innerHTML = user_mention_txt
              }
              

              
          })
      }}

}
user_mention_api_call(user_name)