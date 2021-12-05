let playing = false;
let fingers;
let button;

function setup() {
  createVid();
  //button = createButton('play');
  //button.mousePressed(toggleVid); // attach button listener
  //button.position(windowWidth/2,0);
}

function createVid() {
  let vids = ['https://cdn.glitch.me/8c5ffe26-de70-4cb2-95c0-fe578c2ca8c1%2F1.mp4?v=1638622506678', 'https://cdn.glitch.me/8c5ffe26-de70-4cb2-95c0-fe578c2ca8c1%2F2.mp4?v=1638626881333'];
  let video = random(vids);
  vid = createVideo([video]);
  vid.size(windowWidth/1.2,windowHeight/1.2);
  vid.position(0,windowHeight/15);
  vid.center('horizontal');
  noLoop();
  contVid();
  
}

function contVid() {
  vid.play();
  vid.onended(createVid)
  playing = !playing;
}

function stopVid() {
  vid.stop()
}

