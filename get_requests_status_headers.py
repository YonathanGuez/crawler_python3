import requests
if __name__ == '__main__':
	url = 'https://www.google.com/'
	r = requests.get(url)
	print("\n** Url**")
	print(r.url)
	print("\n** Status code **")
	print(r.status_code)
	print("\n** Headers**")
	print(r.headers)
	print("\n** Cookies **")
	print(vars(r.cookies))
	print("\n** Encoding **")
	print(r.encoding)
	print("\n** History **")
	print(r.history)
	print("\n** Print raw **")
	print(vars(r.raw))
	print("\n** Time Answer in seconds **")
	print(r.elapsed.total_seconds())
	print("\n** Filter **")
	first_nb = str(r.status_code)[0]
	if first_nb == "1":
		print("Information")
		if 100 == r.status_code:
			print("Continue")
		elif 101 == r.status_code:
			print("Switching Protocols")
		elif 102 == r.status_code:
			print("Processing")
		elif 103 == r.status_code:
			print("Early Hints")
	elif first_nb == "2":
		print("Succes")
		if 200 == r.status_code:
			print("OK")
		elif 201 == r.status_code:
			print("Created")
		elif 202 == r.status_code:
			print("Accepted")
		elif 203 == r.status_code:
			print("Non-Authoritative Information")
		elif 204 == r.status_code:
			print("No Content")
		elif 205 == r.status_code:
			print("Reset Content")
		elif 206 == r.status_code:
			print("Partial Content")
		elif 207 == r.status_code:
			print("Multi-Status")
		elif 208 == r.status_code:
			print("Already Reported")
		elif 210 == r.status_code:
			print("Content Different")
		elif 226 == r.status_code:
			print("IM Used")
	elif first_nb == "3":
		print("Redirection")
		if 300 == r.status_code:
			print("Multiple Choices")
		elif 301 == r.status_code:
			print("Moved Permanently")
		elif 302 == r.status_code:
			print("See Other")
		elif 303 == r.status_code:
			print("See Other")
		elif 304 == r.status_code:
			print("Not Modified")
		elif 305 == r.status_code:
			print("	Use Proxy")
		elif 306 == r.status_code:
			print("Switch Proxy")
		elif 307 == r.status_code:
			print("Temporary Redirect")
		elif 308 == r.status_code:
			print("Permanent Redirect")
		elif 310 == r.status_code:
			print("Too many Redirects")
	elif first_nb == "4":
		print("Erreur du client web")
		if 400 == r.status_code:
			print("Bad Request")
		elif 401 == r.status_code:
			print("Unauthorized")
		elif 402 == r.status_code:
			print("Payment Required")
		elif 403 == r.status_code:
			print("Forbidden")
		elif 404 == r.status_code:
			print("Not Found")
		elif 405 == r.status_code:
			print("Method Not Allowed")
		elif 406 == r.status_code:
			print("Not Acceptable")
		elif 407 == r.status_code:
			print("Proxy Authentication Required")
		elif 408 == r.status_code:
			print("Request Time-out")
		elif 409 == r.status_code:
			print("	Conflict")
		elif 410 == r.status_code:
			print("Gone")
		elif 411 == r.status_code:
			print("Length Required")
		elif 412 == r.status_code:
			print("Precondition Failed")
		elif 413 == r.status_code:
			print("Request Entity Too Large")
		elif 414 == r.status_code:
			print("Request-URI Too Long")
		elif 415 == r.status_code:
			print("Unsupported Media Type")
		elif 416 == r.status_code:
			print("Requested range unsatisfiable")
		elif 417 == r.status_code:
			print("Expectation failed")
		elif 418 == r.status_code:
			print("I’m a teapot")
		elif 421 == r.status_code:
			print("Bad mapping")
		elif 422 == r.status_code:
			print("Unprocessable entity")
		elif 423 == r.status_code:
			print("Locked")
		elif 424 == r.status_code:
			print("Method failure")
		elif 425 == r.status_code:
			print("Unordered Collection")
		elif 426 == r.status_code:
			print("Upgrade Required")
		elif 428 == r.status_code:
			print("Precondition Required")
		elif 429 == r.status_code:
			print("Too Many Requests")
		elif 431 == r.status_code:
			print("Request Header Fields Too Large")
		elif 449 == r.status_code:
			print("Retry With")
		elif 450 == r.status_code:
			print("Blocked by Windows Parental Controls")
		elif 451 == r.status_code:
			print("Unavailable For Legal Reasons")
		elif 456 == r.status_code:
			print("Unrecoverable Error")
		elif 444 == r.status_code:
			print("No Response")
		elif 495 == r.status_code:
			print("SSL Certificate Error")
		elif 496 == r.status_code:
			print("SSL Certificate Required")
		elif 497 == r.status_code:
			print("HTTP Request Sent to HTTPS Port")
		elif 498 == r.status_code:
			print("Token expired/invalid")
		elif 499 == r.status_code:
			print("Client Closed Request")
	elif first_nb == "5":
		print("Erreur du serveur")
		if 500 == r.status_code:
			print("Internal Server Error")
		elif 501 == r.status_code:
			print("Not Implemented")
		elif 502 == r.status_code:
			print("Bad Gateway ou Proxy Error")
		elif 503 == r.status_code:
			print("Service Unavailable")
		elif 504 == r.status_code:
			print("Gateway Time-out")
		elif 505 == r.status_code:
			print("HTTP Version not supported")
		elif 506 == r.status_code:
			print("Variant Also Negotiates")
		elif 507 == r.status_code:
			print("Insufficient storage")
		elif 508 == r.status_code:
			print("Loop detected")
		elif 509 == r.status_code:
			print("Bandwidth Limit Exceeded")
		elif 510 == r.status_code:
			print("Not extended")
		elif 511 == r.status_code:
			print("Network authentication required")
		elif 520 == r.status_code:
			print("Unknown Error")
		elif 521 == r.status_code:
			print("	Web Server Is Down")
		elif 522 == r.status_code:
			print("Connection Timed Out")
		elif 523 == r.status_code:
			print("Origin Is Unreachable")
		elif 524 == r.status_code:
			print("A Timeout Occurred")
		elif 525 == r.status_code:
			print("SSL Handshake Failed")
		elif 526 == r.status_code:
			print("Invalid SSL Certificate")
		elif 527 == r.status_code:
			print("Railgun Error")