const title = document.querySelector('input[name=title]');
const slug = document.querySelector('input[name=slug]');

const slugify = (val) => {
    return val.toString().toLowerCase().trim()
    .replace(/&/g, '-and-')                  // convert '&' into '-and-'
    .replace(/[\s\W-]+/g, '-')               // convert spaces, non-words, and dashes into '-' 
}

title.addEventListener( 'keyup', (e) => {
    slug.setAttribute( 'value', slugify(title.value) );
} );


