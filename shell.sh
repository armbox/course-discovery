container=$(node ./tools/container.js)
docker exec -it ${container} env TERM=xterm-256color bash 
