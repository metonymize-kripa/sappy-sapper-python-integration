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
    },
    {
        title: 'What is range?',
        slug: 'tutorial-range',
        html: `
              Using options data we calculate at-the-money implied volatility and use that as a proxy for standard deviation(sigma). Default range is the one that give us the 75% probabilty. If you want 90% probability range use sigma=1.96.
              For more information - <a href="https://en.wikipedia.org/wiki/Normal_distribution#Standard_deviation_and_coverage">Normal Distribution</a>
          `
     },
    {
        title: 'What is doom?',
        slug: 'tutorial-doom',
        html: `
                Using options data we calculate probability of options expiring in the money. For a call that is eqivalent to the probability of stock being over strike and for the put the prob of stock being below the strike. Doom gives us the probability of put expiring in the money.
                For more information - <a href="https://www.macroption.com/delta-calls-puts-probability-expiring-itm/">Delta Approximation</a>
            `
    },
    {
        title: 'What is volume?',
        slug: 'tutorial-volume',
        html: `
                  Using stock volume from past 10 days, we calculate the current level in two ways - as a multiple of average daily volume and as a percentile. Volume numbers during a trading session are scaled appropriately.
                  For more information - <a href="https://finance.yahoo.com/quote/spy">Yahoo Finance</a>
              `
    },
    {
        title: 'What is call?',
        slug: 'tutorial-call',
        html: `
                Using options data we calculate the probabilty of a call option expiring in the money. That probabilty along with premium received gives us an idea of which option has the maximum payoff potential. Similar methodology is used to find the optimal spread trade.
                For more information - <a href="https://finance.yahoo.com/quote/SPY/options?p=SPY">Yahoo Finance</a>
              `
    },
    {
        title: 'What is kelly?',
        slug: 'tutorial-kelly',
        html: `
                Using at-the-money options data we calculate the options implied probabilty of stock going up.  Based on those probabilty we calculate the optimal betting size of stock using Kelly criterion
                For more information - <a href="https://en.wikipedia.org/wiki/Kelly_criterion">Kelly Criterion</a>
              `
    },
    {
        title: 'What is div?',
        slug: 'tutorial-div',
        html: `
                The recent dividend data is displayed along with the dividend yield. Dividend yield is the percentage of money you earn on your stock investment as dividend payout.
                  For more information - <a href="https://finance.yahoo.com/quote/c">Yahoo Finance</a>
              `
    },
];

posts.forEach(post => {
  post.html = post.html.replace(/^\t{3}/gm, '');
});

export default posts;
