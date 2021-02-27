// Ordinarily, you'd generate this data from markdown files in your
// repo, or fetch them from a database of some kind. But in order to
// avoid unnecessary dependencies in the starter template, and in the
// service of obviousness, we're just going to leave it here.

// This file is called `_posts.js` rather than `posts.js`, because
// we don't want to create an `/blog/posts` route — the leading
// underscore tells Sapper not to do that.

const posts = [
  {
    title: 'How can I get involved?',
    slug: 'how-can-i-get-involved',
    html: `
			<p><strong> Sign up for the <a href='https://oracled.mailchimpsites.com/'> DailySpread</a></strong></p>
		`
  },
  {
      title: 'How do I use the tool?',
      slug: 'tutorial-main',
      html: `
            <h1 style="color:blue;"> Type the symbol and hit enter or click Go</h1>
            <figure style='width:80%;margin:0 auto'>
            	<img alt='Type symbol and Go' src='FatNeo_Tutorial_1_1.png'>
            </figure>
            <h1 style="color:blue;"> Enjoy the simplicity </h1>
            <figure style='width:80%;margin:0 auto'>
            	<img alt='Enjoy the data' src='FatNeo_Tutorial_1_2.png'>
            </figure>
        `
    }
];

posts.forEach(post => {
  post.html = post.html.replace(/^\t{3}/gm, '');
});

export default posts;
