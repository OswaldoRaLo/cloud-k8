# cloud-k8

## Iniciar Minikube

#### Para iniciar Minikube, ejecuta el siguiente comando:
```
minikube start
```

## Construir la imagen Docker

#### Para construir la imagen, ejecuta el siguiente comando:
```
docker build -t localhost:5000/api:1
```

## Reenviar el puerto para el registro

#### Para reenviar el puerto, ejecuta el siguiente comando:

```
kubectl port-forward --namespace kube-system service/registry 5000:80
```

## En otra consola ejecutar el contenedor Docker para reenviar el tráfico al registro local

#### Para enviar el tráfico, ejecuta el siguiente comando:
```
docker run --rm -it --network=host alpine ash -c "apk add socat && socat TCP-LISTEN:5000,reuseaddr,fork TCP:host.docker.internal:5000"
```

## Empujar la imagen al registro local

#### Para subir la imagen, ejecuta el siguiente comando:
```
docker push localhost:5000/api:1
```

## Crear los nuevos namespaces, uno para la api y otro para la db

#### Para crear las apis, ejecuta los siguientes comandos:

```
kubectl create namespace apimong

kubectl create namespace dbmongo
```

## Aplicar los archivos de configuración del despliegue

#### Para el despliege, ejecuta los siguientes comandos:

```
kubectl apply -f Deployment.yml

kubectl apply -f Service.yml

kubectl apply -f Dploymentdb.yml

kubectl apply -f Deploymentperistent.yml

kubectl apply -f Servicedb.yml
```

## Obtener los despliegues de ambos namespaces

#### Para obtener los despliegues, ejecuta los siguientes comandos:

```
kubectl get deployments -n apimong

kubectl get deployments -n dbmongo
```

## Obtener los pods de apimong

#### Para obtener el pod, ejecuta el siguiente comando:

```
kubectl get pods -n apimong
```

## Ver los logs del pod específico

#### Para obtener los logs, ejecuta el siguiente comando:

```
kubectl logs <logs>-n apimong
```

## obtener el servicio del namespace

#### Para obtener el servicio, ejecuta el siguiente comando:

```
kubectl get svc -n apimong
```

## Obtener la URL del servicio

#### Para las urls, ejecuta los siguientes comandos:

```
minikube service api -n apimong --url

minikube service cmongo -n dbmongo --url
```

## Mandar a llamar el servicio
#### Para llamar el servicio, ejecuta el siguiente comando:
```
curl http://127.0.0.1:27017/api
```
