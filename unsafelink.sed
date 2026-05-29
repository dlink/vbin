# Unwrap Microsoft Defender / Outlook Safe Links URLs
# Replace Safe Links wrappers with the original URL
#
#   Usage:
#
#     sed -E -f unsafelink.sed api.log | more

s#(https://[^ ]*safelinks\.protection\.outlook\.com/[^ ]*[?&]url=)([^& ]+)([^ ]*)#\2#g
s/%3A/:/Ig
s/%2F/\//Ig
s/%3F/?/Ig
s/%3D/=/Ig
s/%26/\&/Ig
s/%25/%/Ig
s/%23/#/Ig
