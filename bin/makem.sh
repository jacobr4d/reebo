TXT="${1}"
TMP="/tmp/reebo"
FLAC="${TMP}/flac.flac"
MP3="${TMP}/"$(basename "${TXT}").mp3 
mkdir -p /tmp/reebo/
touch "${FLAC}"
say -f "${TXT}" -o "${FLAC}"
ffmpeg -i "${FLAC}" "${MP3}"
open "${MP3}"