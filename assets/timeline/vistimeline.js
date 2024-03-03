var container = document.getElementById("visualization");

var DIR = "assets/timeline/imgs/";

// note that months are zero-based in the JavaScript Date object
var items = new vis.DataSet([
  {
    start: new Date(2024, 7, 23),
    content:
      '<div>Conversation</div><img src="https://icons.iconarchive.com/icons/iconfactory/looney/32/Madador-B-icon.png" style="width:32px; height:32px;">',
  },
  {
    start: new Date(2024, 7, 23, 23, 0, 0),
    content:
      '<div>Mail from boss</div><img src="https://cdn.wikimg.net/en/strategywiki/images/4/40/WD_Babasama.gif" style="width:32px; height:32px;">',
  },
  { start: new Date(2024, 7, 24, 16, 0, 0), content: "Report" },
  {
    start: new Date(2024, 7, 26),
    end: new Date(2024, 8, 2),
    content: "Traject A",
  },
  {
    start: new Date(2024, 7, 28),
    content:
      '<div>Memo</div><img src="https://gadgetsin.com/uploads/2021/03/divoom_pixoo_max_pixel_led_display_1-66x66.jpg" style="width:48px; height:48px;">',
  },
  {
    start: new Date(2024, 7, 29),
    content:
      '<div>Phone call</div><img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.iconsdb.com%2Ficons%2Fpreview%2Fdim-gray%2Fphone-32-xl.png&f=1&nofb=1&ipt=dde3425f8a9454a0655ad8e4a21aaf30c64fcc548ab7c3b6c414b6b088f635a3&ipo=images" style="width:32px; height:32px;">',
  },
  {
    start: new Date(2024, 7, 31),
    end: new Date(2024, 8, 3),
    content: "Traject B",
  },
  {
    start: new Date(2024, 8, 4, 12, 0, 0),
    content:
'<div>Report</div><img src="http://127.0.0.1:43932/assets/timeline/imgs/duck.png" style="width:32px; height:32px;">'
  },
]);

var options = {
  editable: true,
  margin: {
    item: 20,
    axis: 40,
  },
};

var timeline = new vis.Timeline(container, items, options);