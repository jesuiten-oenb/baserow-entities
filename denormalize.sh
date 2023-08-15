add-attributes -g "./data/*/*.xml" -b "https://oenb.ac.at"
add-attributes -g ".data/*/*.xml" -b "https://oenb.ac.at"
denormalize-indices -f "./data/*/*.xml" -i "./data/indices/*.xml" -m ".//*[@key]/@key" -x ".//tei:title[1]/text()"