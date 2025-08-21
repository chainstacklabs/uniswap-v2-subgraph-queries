# AGENTS Guidelines for This Repository

This repository contains GraphQL queries for Uniswap V2 subgraph data analysis. When working on the project interactively with an agent (e.g. the Codex CLI) please follow the guidelines below for efficient querying and data analysis.

## 1. Use Rate-Limited Queries for Development

* **Always test queries individually** before batch execution.
* **Start with small result sets** using `first` parameter.
* **Do _not_ make excessive queries** to avoid rate limiting.
* **Monitor response times** to detect performance issues.

## 2. Keep Dependencies in Sync

If you update dependencies:

1. Update using pip: `pip install -r requirements.txt`.
2. Keep requirements minimal (requests, python-dotenv).
3. Verify compatibility with Python 3.7+.

## 3. Environment Configuration

Create a `.env` file with your subgraph endpoint:

```env
SUBGRAPH_URL=https://your-subgraph-endpoint-here
```

Common endpoints:
- Ethereum: `https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2`
- Other networks: Check The Graph or Chainstack for endpoints

## 4. Query Development Workflow

Follow this workflow for query development:

1. **Test queries**: Use GraphQL playground first
2. **Save queries**: Store in `Queries/` directory as `.graphql` files
3. **Run individually**: Test one query before batch execution
4. **Analyze outputs**: Check `Outputs/` directory for JSON results

## 5. Running Queries

### Individual Query Testing
Test a specific query manually:
```bash
# Run main script for all queries
python main.py
```

### Jupyter Notebook Analysis
Use the notebook for interactive analysis:
```bash
jupyter notebook UniswapV2.ipynb
```

## 6. Query Best Practices

* **Use pagination**: Add `first`, `skip`, and `orderBy` parameters
* **Filter efficiently**: Use `where` clauses to reduce data transfer
* **Request only needed fields**: Minimize response size
* **Handle large datasets**: Use iterative queries with pagination
* **Cache results**: Save outputs to avoid repeated queries

## 7. Common Query Patterns

### Pagination Example
```graphql
{
  swaps(first: 100, skip: 0, orderBy: timestamp, orderDirection: desc) {
    id
    timestamp
    amountUSD
  }
}
```

### Filtering Example
```graphql
{
  pairs(where: {volumeUSD_gt: "1000000"}) {
    id
    token0 { symbol }
    token1 { symbol }
    volumeUSD
  }
}
```

## 8. Output Management

The script automatically:
- Creates `Outputs/` directory if missing
- Saves query results as JSON files
- Names output files based on query names
- Includes execution time metrics

## 9. Query Types Reference

Available query templates in `Queries/`:

| Query File | Purpose |
| ---------- | ------- |
| `subgraph_meta.graphql` | Subgraph metadata and sync status |
| `pairs_largest_reserve.graphql` | Top pairs by reserve |
| `pairs_recently_created.graphql` | Newly created pairs |
| `swaps_latest.graphql` | Recent swap transactions |
| `swaps_latest_for_pair.graphql` | Swaps for specific pair |
| `swaps_latest_large.graphql` | Large value swaps |
| `token_price.graphql` | Current token prices |
| `token_price_historical.graphql` | Historical price data |
| `trading_volume_daily_for_pair.graphql` | Daily volume metrics |
| `trading_volume_hourly_for_pair.graphql` | Hourly volume metrics |
| `uniswap_daily_data.graphql` | Protocol-wide daily stats |
| `liquidity_positions_historical.graphql` | LP position history |
| `liquidity_positions_largest.graphql` | Top liquidity providers |

## 10. Error Handling

Common issues and solutions:

**"Timeout error"**
- Reduce query complexity
- Add pagination with smaller `first` value
- Increase timeout in `main.py` (line 39)

**"Rate limit exceeded"**
- Add delays between queries
- Use a different endpoint
- Reduce query frequency

**"Invalid query"**
- Validate in GraphQL playground first
- Check field names match schema
- Ensure proper nesting structure

## 11. Data Analysis Tips

* **Use Jupyter notebook** for exploratory analysis
* **Export to CSV** for spreadsheet analysis
* **Visualize trends** with matplotlib/plotly
* **Compare time periods** for pattern detection
* **Cross-reference** multiple query results

## 12. Performance Optimization

* Set appropriate timeout values (default: 40 seconds)
* Use specific time ranges in queries
* Limit result sets during development
* Consider caching frequently accessed data
* Batch similar queries when possible

## 13. Useful Commands Recap

| Command | Purpose |
| ------- | ------- |
| `pip install -r requirements.txt` | Install dependencies |
| `python main.py` | Run all queries |
| `jupyter notebook UniswapV2.ipynb` | Open analysis notebook |

## 14. Safety Reminders

* **Never commit API keys** or private endpoints
* **Use public endpoints** for development
* **Respect rate limits** to avoid bans
* **Validate data accuracy** before analysis
* **Keep queries efficient** to minimize costs

---

Following these practices ensures efficient subgraph querying, prevents rate limiting, and maintains data quality. Always test queries in small batches before running comprehensive data collection.