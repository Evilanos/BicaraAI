import 'package:http/http.dart' as http;
import 'dart:convert';

Future<void> addUser(String email, String firstname, String lastname) async {
  final url = 'http://10.0.2.2:5000/add_user';

  final response = await http.post(
    Uri.parse(url),
    headers: {
      'Content-Type': 'application/json',
    },
    body: json.encode({
      'email': email,
      'firstname': firstname,
      'lastname': lastname,
    }),
  );

  if (response.statusCode == 200) {
    print('User added successfully');
  } else {
    throw Exception('Failed to add user');
  }
}
