import 'package:flutter/material.dart';
import '../services/api_service.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {

  late Future<List<dynamic>> projects;

  @override
  void initState() {
    super.initState();
    projects = ApiService.getProjects();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Sudiksha Living"),
      ),
      body: FutureBuilder(
        future: projects,
        builder: (context, snapshot) {

          if (snapshot.connectionState ==
              ConnectionState.waiting) {
            return const Center(
              child: CircularProgressIndicator(),
            );
          }

          if (snapshot.hasError) {
            return Center(
              child: Text(
                snapshot.error.toString(),
              ),
            );
          }

          final data = snapshot.data!;

          return ListView.builder(
            itemCount: data.length,
            itemBuilder: (context, index) {

              final project = data[index];

              return Card(
                margin: const EdgeInsets.all(10),
                child: ListTile(
                  title:
                      Text(project["project_name"] ?? ""),
                  subtitle:
                      Text(project["locality"] ?? ""),
                ),
              );
            },
          );
        },
      ),
    );
  }
}