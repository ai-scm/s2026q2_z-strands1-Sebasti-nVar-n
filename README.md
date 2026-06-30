# Strands Travel Agent - AI Conversational Assistant
Este proyecto es el resultado del laboratorio "Create Advanced AI Agents with Strands SDK and Amazon Bedrock", donde se desarrolló un agente de viajes inteligente capaz de gestionar vuelos, consultar clima en tiempo real, mantener memoria conversacional y acceder a bases de conocimiento privadas mediante RAG.

# s2026q2a-strands1-Sebasti-nVar-n/
```

├── src/
│   ├── lambda_function.py      # Código principal del agente
│   ├── requirements.txt        # Dependencias (strands, strands-tools, etc.)
│   └── strands/                # Carpeta de la librería 
├── template.yaml               # Definición de la infraestructura (AWS SAM)
├── samconfig.toml              # Configuración de despliegue de SAM
├── seattletouroperators.txt    # Datos de la base de conocimientos (RAG)
├── .gitignore                  # Archivos ignorados (.aws-sam/, response.json)
└── README.md                   # Documentación del proyecto
```
# 🧪 Descripción del Proyecto
El agente fue construido utilizando el SDK de Strands y Amazon Bedrock, implementado en una arquitectura serverless sobre AWS Lambda y gestionado con AWS SAM (Serverless Application Model).

# Características principales:
Gestión de Vuelos: Búsqueda dinámica de opciones de aerolíneas.

Integración de API: Consulta del clima en tiempo real mediante el Servicio Meteorológico Nacional.

Memoria Persistente: Administración de sesiones de chat mediante Amazon DynamoDB para recordar el contexto de conversaciones anteriores.

RAG (Retrieval-Augmented Generation): Acceso a datos privados de operadores turísticos almacenados en Amazon S3 y vectorizados mediante Amazon Bedrock Knowledge Bases.

# 💡 Conceptos Clave
¿Qué es Strands?
Strands es un framework diseñado para la construcción de agentes de IA. A diferencia de otros servicios, permite un control granular sobre las herramientas, el sistema de prompts y la lógica del flujo de trabajo, facilitando la creación de agentes altamente especializados que interactúan con sistemas externos.

Diferencia: Strands SDK vs. Agentes Administrados (Agent Core/AWS)
Strands SDK: Ofrece un enfoque orientado al desarrollo donde tú tienes el control total sobre el ciclo de vida del agente, la lógica de las herramientas y la orquestación. Es ideal para desarrolladores que necesitan personalización profunda.

Agentes Administrados (AWS Bedrock Agents): La orquestación, el manejo de memoria y la invocación de herramientas son gestionadas principalmente por la plataforma de AWS. Es ideal para una implementación rápida con menos mantenimiento de infraestructura.

# 🛠️ Arquitectura Técnica
Modelo de IA: us.amazon.nova-lite-v1:0 vía Amazon Bedrock.

Infraestructura: AWS SAM, AWS Lambda (Python 3.13).

Base de Datos: Amazon DynamoDB (Session Storage).

RAG: Amazon Bedrock Knowledge Bases + Amazon S3.

# 🚀 Despliegue
Para desplegar esta aplicación en tu propia cuenta de AWS:

Clona este repositorio.

Configura las variables de entorno necesarias.

Ejecuta los comandos de SAM:

Bash
sam build --use-container
sam deploy --parameter-overrides KnowledgeBaseId=<TU_KB_ID>
Autor: [Tu Nombre Completo]
Semillero: [Nombre del Semillero]
Fecha: Junio 2026
