for pod in $(kubectl get pods -n shuffle -o name); do
  echo "===> $pod"
  kubectl exec -n shuffle "$pod" -- df -h
  echo ""
done
