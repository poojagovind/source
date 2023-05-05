For the given stream of message requests and their timestamps as input, you must implement a logger rate limiter system that decides whether the current message request is displayed. The decision depends on whether the same message has already been displayed in the last S seconds. If yes, then the decision is FALSE, as this message is considered a duplicate. Otherwise, the decision is TRUE.


class RequestLogger:

    # initailization of requests hash map
    def __init__(self, time_limit):
        self.requests = {}
        self.limit = time_limit

    # function to accept and deny message requests
    def message_request_decision(self, timestamp, request):

        # checking whether the specific request exists in
        # the hash map or not if it exists, check whether its
        # time duration lies within the defined timestamp
        if request not in self.requests or timestamp - self.requests[request] >= self.limit:

            # store this new request in the hash map, and return true
            self.requests[request] = timestamp
            return True

        else:
            # the request already exists within the timestamp
            # and is identical, request should
            # be rejected, return false
            return False

