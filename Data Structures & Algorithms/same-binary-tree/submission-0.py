class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 1. Caso base: ambos são None?
        if not p and not q:
            return True
        
        # 2. Casos de falha: um é None ou valores são diferentes?
        # Dica: if not p or not q or p.val != q.val: ...
        if not p or not q or p.val != q.val:
            return False
        # 3. Se chegou aqui, os nós atuais são iguais! 
        # Agora delegue para os filhos e use o operador 'and'
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)