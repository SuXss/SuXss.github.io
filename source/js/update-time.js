(function() {
  var times = document.getElementsByTagName('time');
  if (times.length === 0) { return; }
  var posts = document.getElementsByClassName('post-content');
  if (posts.length === 0) { return; }

  var pubTime = new Date(times[1].dateTime);  /* 文章发布时间戳 */
  var now = Date.now()  /* 当前时间戳 */
  var interval = parseInt(now - pubTime)
  /* 发布时间超过指定时间（毫秒） */
    var days = parseInt(interval / 86400000)
    posts[0].innerHTML = '<div class="note note-info" style="font-size:0.9rem"><p>' +
      '本文最后更新于 ' + days + ' 天前' +
      '</p></div>' + posts[0].innerHTML;
})();