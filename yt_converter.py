import subprocess

def convert_to_channel_id(url):
    """Converts a given YouTube URL to its channel ID URL format."""

    # Check if the URL is already in the correct format
    if url.startswith("https://www.youtube.com/channel/"):
        channel_id = url
        conversion_status = "SUCCESS"
        conversion_message = url
    else:
        # Run yt-dlp to get the channel URL
        output = subprocess.run(['yt-dlp', '--playlist-items', '0', '-O', 'playlist:channel_url', url], capture_output=True, text=True)
        if output.returncode == 0:
            channel_id = output.stdout.strip()
            conversion_status = "SUCCESS"
            conversion_message = output.stdout.strip()
        else:
            if "HTTP Error 404" in output.stderr:
                conversion_status = "ERROR"
                conversion_message = "HTTP Error 404: Not Found"
                channel_id = ""
            else:
                conversion_status = "ERROR"
                conversion_message = output.stderr.strip()
                channel_id = ""

    # Validate the channel URL
    if channel_id:
        validation = subprocess.run(['yt-dlp', '-s', '--playlist-items', '1', channel_id], capture_output=True)
        validation_status = "ERROR" if validation.returncode != 0 else "SUCCESS"
    else:
        validation_status = "ERROR"

    result = {
        "url": url,
        "conversion_status": conversion_status,
        "conversion_message": conversion_message,
        "validation_status": validation_status
    }

    return result
