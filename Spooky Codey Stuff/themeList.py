themes = {
"light" : {
"setup" : "black", "snake" : "dark green", "cherry" : "red", "background" : "white",
"text" : "black", "highscore" : "black", "line" : "dark gray", "settings" : "black"
},
"dark" : {
"setup" : "white", "snake" : "orange", "cherry" : "light blue", "background" : "black",
"text" : "white", "highscore" : "white", "line" : "gray", "settings" : "white"
},
"gray" : {
"setup" : "light gray", "snake" : "gray", "cherry" : "white", "background" : "dark gray",
"text" : "light gray", "highscore" : "light gray", "line" : "gray", "settings" : "light gray"
},
"classic" : {
"setup" : "black", "snake" : "black", "cherry" : "red", "background" : "white",
"text" : "black", "highscore" : "black", "line" : "white", "settings" : "black"
},
"idle" : {
"setup" : "white", "snake" : "#EA9337", "cherry" : "#6BEF4A", "background" : "#124779",
"text" : "white", "highscore" : "white", "line" : "white", "settings" : "white"
},
"valentines" : {
"setup" : "#9400F4", "snake" : "white", "cherry" : "#9400F4", "background" : "#DD9DFF",
"text" : "#9400FF", "highscore" : "#9400F4", "line" : "white", "settings" : "#9400F4"
},
"sunset" : {
"setup" : "#FA6D6F", "snake" : "#FA6D6F", "cherry" : "#FA006F", "background" : "#FAB96F",
"text" : "#FA6D6F", "highscore" : "#FA6D6F", "line" : "white", "settings" : "#FA6D6F"
},
"vaporwave" : {
"setup" : "#94D0FF", "snake" : "#FF6AD5", "cherry" : "#94D0FF", "background" : "#C774E8",
"text" : "white", "highscore" : "white", "line" : "white", "settings" : "#94D0FF"
},
"spooktober" : {
"setup" : "#E88A1A", "snake" : "#E88A1A", "cherry" : "#CF3030", "background" : "#141414",
"text" : "dark gray", "highscore" : "dark gray", "line" : "dark gray", "settings" : "dark gray"
}
}
themeIndex = []
for item in themes:
    themeIndex.append("%s" % item)
