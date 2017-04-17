Parking App API:

Assume that we are building a parking app for SF city and we need two API's.

Build the following REST APIs. (choose Django or Flask framework. DB is of your choice.)

1. REST API to list all **available** parking spots.
- Input params: {lat, lng, radius}
response: returns an array of elements each containing an id, lat and lng.

2. REST API to reserve an available parking spot. input params: { parking_spot, time-range }

Note: You can store a dummy lat, lng locations in your table.

Optional:
- test cases for the API's
- view existing reservations
- cancel existing reservations
- extend existing reservations.

Deliverables:

* Please host the code in a git repo and share the link with me.
* Commit every logical step.