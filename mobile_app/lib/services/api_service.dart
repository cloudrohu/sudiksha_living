import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {

  static const String baseUrl =
      "http://127.0.0.1:8000/api/projects/";

  static Future<List<dynamic>> getProjects() async {

    final response = await http.get(
      Uri.parse(baseUrl),
    );

    if (response.statusCode == 200) {
      return jsonDecode(response.body);
    }

    throw Exception("Failed to load projects");
  }
}