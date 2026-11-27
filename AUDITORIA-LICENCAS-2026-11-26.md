# Auditoria de licenças e atribuições — 26/11/2026

Projeto: freight-connect. Responsável declarado: João Victor da Silva (JustJao1).

Revisão documental dos arquivos acessíveis no GitHub. Preserva os avisos existentes e os direitos de terceiros; não concede nova licença ao código próprio nem certifica conformidade integral. Nenhuma alteração em código executável ou contrato de serviço.

- requirements.txt declara biblioteca padrão Python.
- public/index.html referencia Leaflet 1.9.4 via unpkg; BSD-2-Clause conforme aviso existente. Preservar licença e copyright: https://github.com/Leaflet/Leaflet/blob/v1.9.4/LICENSE .
- OpenStreetMap: manter atribuição visível e cumprir ODbL, inclusive condições de redistribuição de banco de dados derivado: https://www.openstreetmap.org/copyright . Tiles: https://operations.osmfoundation.org/policies/tiles/ (caching, identificação, proibição de download em massa e limites de capacidade).
- Serviço público router.project-osrm.org é distinto da licença do código OSRM: https://github.com/Project-OSRM/osrm-backend/wiki/Demo-server . Não presumir capacidade ou garantia para produção.
- Dados de municípios: public/municipios-LICENSE.txt contém licença MIT e copyright 2016 Kelvin S. do Prado, conferir preservação na distribuição.
- Google Fonts Lexend e Public Sans; preservar licença específica ao incorporar arquivos.
- Pendência: auditar uso real de tiles/rotas e atribuição visível em produção, não apenas no HTML. Não contratar provedor pago sem autorização.

A tag autoria-2026-11-26 foi consultada na API GitHub: assinatura válida (verified=true, reason=valid), apontando para a versão documentada em EVIDENCIA-2026-11-26.md. A auditoria atual é posterior à versão assinada; seu commit não foi assinado com a chave pessoal do mantenedor.
