import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

# Chiffre d'affaires
données["chiffre_affaires"] = données["prix"]*données["qte"]

# a- Ventes par produit
ventes_prod = données.groupby("produit", as_index=False)["qte"].sum()

# b- Chiffre d'affaires par produit
ca_prod = données.groupby("produit", as_index=False)["chiffre_affaires"].sum()

# Graphiques
# Pie chart: Ventes par region
figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')
figure.update_layout(title_x=0.5, title_font= dict(size=25))
figure.write_html('ventes-par-region.html')

# a- Bar chart: Ventes par produit

figure_a = px.bar(ventes_prod, x="produit", y="qte", title="Ventes par produit",
    labels={"produit":"Produits", "qte":"Quantité vendue"})
figure_a.update_layout(title_x=0.5,
                       xaxis_title_font=dict(size=20),
                       yaxis_title_font=dict(size=20),
                       xaxis_tickfont=dict(size=16),
                       title_font=dict(size=25)
                    )
figure_a.write_html('ventes-par-produit.html')

# b- Bar chart: Chiffre d'affaires par produit
figure_b = px.bar(ca_prod, x="produit", y="chiffre_affaires", title="Chiffre d'affaires par produit",
    labels={"produit":"Produits", "chiffre_affaires":"Chiffre affaires"})
figure_b.update_layout(title_x=0.5,
                       xaxis_title_font=dict(size=20),
                       yaxis_title_font=dict(size=20),
                       xaxis_tickfont=dict(size=16),
                       title_font=dict(size=25)
                    )
figure_b.write_html('chiffre_affaires-par-produit.html')


print('ventes-par-région.html généré avec succès !')
print('ventes-par-produit.html généré avec succès !')
print('chiffre_affaires-par-produit.html généré avec succès !')


