<div align="center">
<img src="./profile_animation.svg" width="100%"/>
</div>
```

O README **não recebe o código Python** — ele só aponta para o SVG que o Python vai gerar.

---

## Estrutura final do repositório:
```
pedropaulucci27/
├── README.md              ← só o markdown
├── generate_svg.py        ← o script Python
├── profile_animation.svg  ← gerado automaticamente pelo Action
└── .github/
    └── workflows/
        └── generate.yml   ← o GitHub Action
